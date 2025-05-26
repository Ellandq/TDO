const request = require('supertest');
const app = require('./app');

describe('GET /health', () => {
    it('responds with status OK', async () => {
        const response = await request(app).get('/health');
        expect(response.statusCode).toBe(200);
        expect(response.body).toEqual({ status: 'OK' });
    });
});